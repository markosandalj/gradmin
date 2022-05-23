const viewType = ( view ) => {
    console.log('Checking view type: ', view)
    const print_preview = (view === 'print_preview')
    const editing = (view === 'editing')
    const standard = (view === 'editing')

    return { print_preview, editing, standard }
}

export default viewType;