export const baseApiRoute = window.location.origin + '/api';
export const baseDjangoAdminRoute = window.location.origin + '/admin';
export const baseWagtailAdminRoute = window.location.origin + '/cms';
export const baseIndexlAdminRoute = window.location.origin + '/index';

export const allMaturasListApiRoute = baseApiRoute + '/matura/all'
export const SectionListApiRoute = baseApiRoute +  '/section/all'
export const SubjectListApiRoute = baseApiRoute + '/subject/all'
export const SkriptaListApiRoute = baseApiRoute + '/skripta/all'

// displays list of all sections inside a Skripta object

export const MaturaFullApiRoute = baseApiRoute + '/matura/' // + maturaId
export const skriptaFullApiRoute = (skriptaId, sectionId) => sectionId ? baseApiRoute + `/skripta/${skriptaId}/${sectionId}` : baseApiRoute +  `/skripta/${skriptaId}`
export const cheatsheetFullApiRoute = (id) => baseApiRoute + `/cheatsheets/${id}`

export const importerApiRoute = baseApiRoute + '/problems_importer'
export const importerUpdateApiRoute = baseApiRoute + '/problems_importer/update'

export const maturaListApiRoute = (subjectId) => baseApiRoute + `/matura/${subjectId}/list`
export const SkriptaSectionListApiRoute = (skriptaId) => baseApiRoute + `/skripta/${skriptaId}/list`

export const cheatsheetsListApiRoute = baseApiRoute + '/cheatsheets/list'

export const ProblemsAdminRoute = baseDjangoAdminRoute + '/problems/problem'