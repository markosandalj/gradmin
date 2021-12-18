import Alpine from 'alpinejs';
window.Alpine = Alpine;

Alpine.data('equationsData', (data) => ({
    equations: data,
    activeEquation: '',
    modalOpen: false,
    filteredEquations: null,

    toggleModal(equation = null) {
        this.activeEquation = equation ? equation : '';
        this.modalOpen = !this.modalOpen;

        setTimeout( () => {
            MathJax.typeset()
        }, 300)
    },
    isModalOpen() {
        return this.modalOpen
    },
    getEquations() {
        return this.filteredEquations && this.filteredEquations.length !== this.equations.length ? this.filteredEquations : this.equations;
    },
    formatEquation(equation) {
        return `$ ${equation.fields.equation} $`
    },
    getActiveEquation() {
        return this.activeEquation.fields
    },
    filterEquations(searchTerm) {
        this.filteredEquations = this.equations.filter(equation => equation.fields.name.includes(searchTerm) )
        
        setTimeout( () => {
            MathJax.typeset()
        }, 300)
    }

}))
 
Alpine.start()
