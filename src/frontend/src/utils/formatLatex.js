export const formatLatex = (string) =>  {
    const strippedString = string.replace(' ', '')

    if(strippedString.startsWith('(/') || strippedString.startsWith('$')) return string

    return '$ ' + string + ' $'
}