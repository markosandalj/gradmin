import React, { useState } from "react";
import { Prompt } from "react-router-dom";
import axios from "axios";

// SHOPIFY
import { Card, ResourceList, ResourceItem, Button, ButtonGroup, TextStyle } from '@shopify/polaris'

// COMPONENTS
import ProblemsTableItem from "./ProblemsTableItem";
import { ViewSwitcher } from "../ViewSwitcher";

// CONSTANTS
import { CRITICAL, SORT_CONFIDENCE_HIGHEST, SORT_CONFIDENCE_LOWEST, SORT_PROBLEMS_NUMBER_DESC, SUCCESS } from "../../settings/constants";
import { importerUpdateApiRoute } from '../../settings/apiRoutes'

// REDUX
import { useDispatch, useSelector } from "react-redux";
import { setUploadInProgress, setUploadIsDone, setItems, sortItems } from "../../store/importerSlice";
import { showBanner } from "../../store/bannerSlice";


export default function ProblemsTable({}) {
    const dispatch = useDispatch()
    const { selectedMatura, selectedSection, selectedSkritpa, selectedSubject, isUploadDone, items: problems } = useSelector(store => store.importer)
    const [ selectedItems, setSelectedItems ] = useState([]);
    const [sortValue, setSortValue] = useState(SORT_PROBLEMS_NUMBER_DESC);

  
    const handleCancle = (event) => {
      event.preventDefault();
      setExistingProblems([])
      setSelectedItems([])

      // handleSubmit(event);
    }

    const handleSubmit = (e) => {
      e.preventDefault();
      
      let formData = new FormData();

      formData.append('data', 
        JSON.stringify({ 
          problems: problems, 
          matura: selectedMatura,
          skripta: selectedSkritpa,
          subject: selectedSubject,
          section: selectedSection 
      }))

      dispatch(setUploadInProgress())

      axios.post(
              importerUpdateApiRoute,
              formData,
              { headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"} }
          )
          .then(res => res.data)
          .then(data => {
            dispatch(showBanner({ 
              title: 'Zadaci uspješno uploadani. Bravo!',
              status: SUCCESS,
              message: 'U adminu možeš provjeriti jesu svi zadaci stvarno na broju'
            }))
            window.scrollTo(0, 0)
          })
          .catch(err => {
            console.log(err)
            dispatch(showBanner({ 
              title: 'Something failed!',
              status: CRITICAL,
              message: err.message
            }))
          })
          .finally(() => {
            dispatch(setUploadIsDone())
          })
  }

  const resourceName = {
    singular: 'zadatak',
    plural: 'zadataka',
  };

  const promotedBulkActions = [
    {
      content: 'Delete problems',
      onAction: () => {
        dispatch(setItems(problems.filter(item => !selectedItems.includes(item.id) )))
        setSelectedItems([])
      }
    }
  ];
    
  const bulkActions = [];
    
  const renderItem = (item) => {
    const { image, mathpix_response, id } = item;
    const text = mathpix_response.text;
    const line_data = mathpix_response.line_data;
    const confidence = Math.round((mathpix_response.confidence + Number.EPSILON) * 100);
    const confidence_rate = Math.round((mathpix_response.confidence_rate + Number.EPSILON) * 100);
  
    return (
        <ResourceItem id={id}>
          <ProblemsTableItem 
            id={id}
            text={text} 
            image={image} 
            line_data={line_data} 
            confidence={confidence} 
            confidence_rate={confidence_rate}
          />
        </ResourceItem>
    )
  }

  return (
    <>
      <Card
        secondaryFooterActions={[{ 
            content: "Cancle", 
            destructive: true, 
            onClick: handleCancle, 
            disabled: !isUploadDone || !selectedMatura || !selectedSkritpa || !selectedSubject 
        }]}
        primaryFooterAction={{ 
          content: "Submit", 
          onClick: handleSubmit, 
          disabled: !isUploadDone || !selectedMatura || !selectedSkritpa || !selectedSubject 
        }}
      >
          <ResourceList
            resourceName={resourceName}
            items={problems}
            renderItem={renderItem}
            selectedItems={selectedItems}
            onSelectionChange={setSelectedItems}
            promotedBulkActions={promotedBulkActions}
            bulkActions={bulkActions}
            sortValue={sortValue}
            sortOptions={[
              {label: 'Lowest confidence', value: SORT_CONFIDENCE_LOWEST},
              {label: 'Highest confidence', value: SORT_CONFIDENCE_HIGHEST},
              {label: 'Problem number', value: SORT_PROBLEMS_NUMBER_DESC},
            ]}
            onSortChange={(selected) => {
              setSortValue(selected);
              dispatch(sortItems(selected))
            }}
            filterControl={<ViewSwitcher edit />}
          />
          <Card.Section>
            {(!selectedMatura || !selectedSkritpa || !selectedSubject) && 
              <TextStyle variation="negative">
                Potrebno je unjeti Skriptu, Maturu i Predmet da bi se moglo submitat
              </TextStyle>}
          </Card.Section>
      </Card>
    </>
  )
}