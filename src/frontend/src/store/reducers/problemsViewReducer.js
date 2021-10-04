import * as actions from '../actions/actionTypes';

const ProblemsView = (view = {}, action) => {
    switch (action.type) {
        case actions.TOGGLE_EDITING:
            view.editing = view.editing ? !view.editing : action.payload.editing
            return {...view}
        case actions.TOGGLE_PRINT_PREVIEW:
            view.printing = view.printing ? !view.printing : action.payload.printing
            return {...view}
        case actions.TOGGLE_SITE_PREVIEW:
            view.site_preview = view.site_preview ? !view.site_preview : action.payload.site_preview 
            return {...view}
        // case actions.TOGGLE_MATURA_LIST:
        //     view.site_preview = view.site_preview ? !view.site_preview : action.payload.site_preview 
        //     return {...view}
        default:
            return view
    }
}

export default ProblemsView;