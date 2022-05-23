import * as actions from '../actions/actionTypes';

const PageViewReducer = (view = '', action) => {
    switch (action.type) {
        case actions.TOGGLE_EDITING:
            return 'editing'

        case actions.TOGGLE_PRINT_PREVIEW:
            return 'print_preview'

        case actions.TOGGLE_SITE_PREVIEW:
            return 'standard'

        default:
            return 'standard'
    }
}

export default PageViewReducer;