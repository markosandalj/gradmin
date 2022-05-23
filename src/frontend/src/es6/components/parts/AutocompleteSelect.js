import React, { Component, useState, useEffect, useCallback } from "react";
import { useParams } from 'react-router';
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";

// SHOPIFY
import {Autocomplete, Icon, TextField } from '@shopify/polaris';
import {SearchMinor} from '@shopify/polaris-icons';

export default function AutocompleteSelect({ apiUrl, label, setData, data }) {
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [deselectedOptions, setDeselectedOptions] = useState([])
  const [options, setOptions] = useState([]);

  useEffect(() => {
    if(apiUrl) {
      axios.get(window.location.origin + apiUrl)
        .then(res => res.data)
        .then(data => {
          let reducedData = []

          data.map((item) => {
            reducedData.push({
              value: item.id.toString(),
              label: item?.name || `${item.subject.subject_name} ${item.subject.level != '0' ? item.subject.level : ''} ${item.year.year}., ${item.term.term}`,
            })
          })
      
          setDeselectedOptions(reducedData)
          setOptions(reducedData)
        })
        .catch(err => console.log(err))
    }

    if(data) {
      let reducedData = []
      data.map((item) => {
        reducedData.push({
          value: item.id.toString(),
          label: item?.name
        })
      })
      setDeselectedOptions(reducedData)
      setOptions(reducedData)
    }
  }, [])
  
    const updateText = useCallback(
      (value) => {
        setInputValue(value);
  
        if (value === '') {
          setOptions(deselectedOptions);
          return;
        }
  
        const filterRegex = new RegExp(value, 'i');
        const resultOptions = deselectedOptions.filter((option) =>
          option.label.match(filterRegex),
        );
        setOptions(resultOptions);
      },
      [deselectedOptions],
    );
  
    const updateSelection = useCallback(
      (selected) => {
        const selectedValue = selected.map((selectedItem) => {
          const matchedOption = options.find((option) => {
            return option.value.match(selectedItem);
          });
          
          return matchedOption && matchedOption.label;
        });
  
        setSelectedOptions(selected);
        setData(selected);
        setInputValue(selectedValue[0]);
      },
      [options],
    );
  
    const textField = (
      <Autocomplete.TextField
        onChange={updateText}
        label={label}
        value={inputValue}
        prefix={<Icon source={SearchMinor} color="base" />}
        placeholder="Search"
      />
    );
  
    return (
      <div style={{height: '225px'}}>
        <Autocomplete
          options={options}
          selected={selectedOptions}
          onSelect={updateSelection}
          textField={textField}
        />
      </div>
    );
  }