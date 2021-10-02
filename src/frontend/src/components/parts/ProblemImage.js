// REACT & REDUX
import React, { useState, useCallback, useEffect } from "react";
import { useSelector } from 'react-redux';

// SHOPIFY
import { DropZone } from '@shopify/polaris';

// FONTAWESOME
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPen} from '@fortawesome/free-solid-svg-icons'

const ProblemImage = ({image}) => {
    const [imageSrc, setImgSrc] = useState(image.image)
    const [hasChanged, setHasChanged] = useState(false)
    const [editImageFieldOpen, setEditImageFieldOpen] = useState(false);
    const [file, setFile] = useState();
    const view = useSelector( state => state?.problems_view )

    const handleEditImageFieldToggle = () => {
        if(editImageFieldOpen && hasChanged) {
            mathTypeset()
        }
        setEditImageFieldOpen(
            (editImageFieldOpen) => !editImageFieldOpen
        ) 
    }

    const handleDropZoneDrop = useCallback(
        (_dropFiles, acceptedFiles, _rejectedFiles) =>
            setFile((file) => acceptedFiles[0]),  
        [],
    );

    useEffect( () => {
        if(file) {
            setImgSrc( window.URL.createObjectURL(file))
        }
    }, [file])

    const validImageTypes = ['image/gif', 'image/jpeg', 'image/png'];
        
    const fileUpload = !file && <DropZone.FileUpload />;

    return (
        <div className='problem__image-container'>
            <img className='problem__image' src={imageSrc} />
            {view.editing && 
                <button type="button" className={ `problem__image-edit ${editImageFieldOpen ? 'open' : ''}`} onClick={handleEditImageFieldToggle}>
                    <FontAwesomeIcon icon={faPen} />
                </button>
            }
            {view.editing && editImageFieldOpen && <DropZone accept="image/*" type="image" allowMultiple={false} onDrop={handleDropZoneDrop}>
                {fileUpload}
                {file && file.name}
            </DropZone>}
        </div>
    )
}

export default ProblemImage;