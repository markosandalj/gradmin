import React, { useMemo, useState } from 'react'

// SHOPIFY
import { TextField, Stack, Icon } from '@shopify/polaris'
import { EditMinor } from "@shopify/polaris-icons";

// REDUX 
import { useDispatch, useSelector } from 'react-redux'
import { showSaveBar } from '../store/saveBarSlice';

// CONSTANTS
import { EDITING_VIEW_TYPE } from '../settings/constants'

// UTILS
import { mathjaxTypeset } from '../utils/mathjaxTypeset'
import throttle from 'lodash.throttle'
import { FloatingEditButton } from './FloatingEditButton';


export const EditableTextField = ({ value, label, id, children, containsMath, onChangeFn, index }) => {
    const { viewType } = useSelector(store => store.view)
    
    const [currentValue, setCurrentValue] = useState(value)
    const [hasChanged, setHasChanged] = useState(false)
    const [isOpen, setIsOpen] = useState(false)

    const dispatch = useDispatch()

    const handleChange = (newValue, id) => {
        setCurrentValue(newValue)
        setHasChanged(true)
        onChangeFn({ id: id, value: newValue, index: index })
        dispatch(showSaveBar())
    };

    const setValueWithMath = () => {
        return { __html: `${currentValue}` };
    }

    const toggleField = () => {
        setIsOpen(!isOpen)

        if(hasChanged) mathjaxTypeset();
    }

    const throttledChangeHandler = useMemo(
        () => throttle(handleChange, 100)
    , []);

    if(!currentValue) return <></>;
    
    return (
        <Stack vertical>
            <Stack.Item fill>
                <Stack wrap={false}>
                    <Stack.Item fill>
                        {label} 
                        {containsMath ? 
                            <span dangerouslySetInnerHTML={setValueWithMath()}></span> 
                            : currentValue}
                    </Stack.Item>
                    <Stack.Item>
                        {children}
                    </Stack.Item>
                    <Stack.Item>
                        {viewType === EDITING_VIEW_TYPE &&
                            <FloatingEditButton onClick={toggleField}>
                                <Icon source={EditMinor} />
                            </FloatingEditButton>}
                    </Stack.Item>
                </Stack>
            </Stack.Item>
            <Stack.Item fill>
                <Stack vertical>
                    {viewType === EDITING_VIEW_TYPE && isOpen &&
                        <Stack.Item fill>
                            <TextField
                                value={currentValue}
                                onChange={throttledChangeHandler}
                                readOnly={false}
                                multiline={4}
                                id={id}
                            />
                        </Stack.Item>}
                </Stack>
            </Stack.Item>
        </Stack>
    )
}
