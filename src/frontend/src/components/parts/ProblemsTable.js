// REACT & REDUX
import React, { Component, useState, useEffect, useCallback } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

import { Card, ResourceList, ResourceItem, Button, ButtonGroup } from '@shopify/polaris'
import ProblemsTableItem from "./ProblemsTableItem";

export default function ProblemsTable({ problems, info }) {
    const [ selectedItems, setSelectedItems ] = useState([]);
    const [ existingProblems, setExistingProblems ] = useState( problems.map(item => ({ ...item, id: item.mathpix_response.request_id})) )
    const [formData, setFormData] = useState( { ...info, problems: [] } );
    const [sortValue, setSortValue] = useState('PROBLEMS_NUMBER_DESC');

    useEffect(() => {
      setFormData({
        ...formData,
        ...info
      })
    }, [info])

    const handleCancle = (event) => {
      event.preventDefault();
      setExistingProblems([])
      setSelectedItems([])

      handleSubmit(event);
    }

    const handleSubmit = (event) => {
      event.preventDefault();
      setFormData({
        ...formData,
        problems: formData.problems.filter(problem => existingProblems.some(p => p.id === problem.id))
      })
      console.log('formData: ', formData)

      let data = new FormData();

      data.append('data', JSON.stringify(formData))

      axios.post(
              window.location.origin + '/api/problems_importer/update',
              data,
              { headers: {'X-CSRFToken': csrftoken, "Content-type": "multipart/form-data"} }
          )
          .then(res => res.data)
          .then(data => console.log(data))
          .catch(err => console.log(err))
  }

    const resourceName = {
        singular: 'zadatak',
        plural: 'zadataka',
      };

      const promotedBulkActions = [
        {
          content: 'Delete problems',
          onAction: () => {
            setExistingProblems(existingProblems.filter(problem => !selectedItems.includes(problem.id) ))
            setSelectedItems([])
          }
        },
        {
          content: 'Approve problem',
          onAction: () => console.log('Todo: implement bulk Approve problem'),
        },
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
                formData={formData} 
                setFormData={setFormData}></ProblemsTableItem>
            </ResourceItem>
        );
    }

    return (
        <Card>
            <ResourceList
                resourceName={resourceName}
                items={existingProblems}
                renderItem={renderItem}
                selectedItems={selectedItems}
                onSelectionChange={setSelectedItems}
                promotedBulkActions={promotedBulkActions}
                bulkActions={bulkActions}
                sortValue={sortValue}
                sortOptions={[
                  {label: 'Lowest confidence', value: 'CONFIDENCE_LOWEST'},
                  {label: 'Highest confidence', value: 'CONFIDENCE_HIGHEST'},
                  {label: 'Problem number', value: 'PROBLEMS_NUMBER_DESC'},
                ]}
                onSortChange={(selected) => {
                  console.log('prije: ', existingProblems);
                  setSortValue(selected);
                  setExistingProblems(
                    existingProblems.sort((a, b) => {
                      if(selected === 'CONFIDENCE_HIGHEST') return b.mathpix_response.confidence - a.mathpix_response.confidence
                      if(selected === 'CONFIDENCE_LOWEST') return a.mathpix_response.confidence - b.mathpix_response.confidence
                    }))
                  console.log(`Sort option changed to ${selected}.`);
                  console.log('poslije: ', existingProblems);
                }}
                // showHeader
            ></ResourceList>
            <div className="py-2 flex-end">
                <ButtonGroup>
                    <Button destructive onClick={handleCancle}>Cancle</Button>
                    <Button primary onClick={handleSubmit}>Submit</Button>
                </ButtonGroup>
            </div>
        </Card>
    )

}