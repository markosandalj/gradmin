import React from 'react'
import { Routes, Route } from 'react-router-dom'

// SETTINGS
import { baseIndexlAdminRoute } from '../settings/apiRoutes'

// COMPONENTS
import { MaturaList } from './pages/MaturaList'
import { MaturaProblems } from './pages/MaturaProblems'
import { SkriptaSectionList } from './pages/SkriptaSectionList'
import { Skripta } from './pages/Skripta'
import { Cheatsheet } from './pages/Cheatsheet'
import { CheatsheetsList } from './pages/CheatsheetsList'
import ProblemsImporter from './pages/ProblemsImporter'


const RouteSwitcher = () => {
  return (
    <Routes>
        <Route 
            path={baseIndexlAdminRoute}
        />
        <Route 
            path="/index/matura/:subject_id/list"
            element={<MaturaList />}
        />
        <Route 
            path="/index/matura/:matura_id"
            element={<MaturaProblems />}
        />
        <Route 
            path="/index/skripta/:skripta_id/list"
            element={<SkriptaSectionList />}
        />
        <Route 
            path="/index/skripta/:skripta_id/:section_id/:section_order"
            element={<Skripta />}
        />
        <Route 
            path="/index/skripta/:skripta_id"
            element={<Skripta />}
        />
        <Route 
            path="/index/problems_importer"
            element={<ProblemsImporter />}
        />
        <Route 
            path="/index/cheatsheets/list"
            element={<CheatsheetsList />}
        />        
        <Route 
            path="/index/cheatsheets/:cheatsheet_id"
            element={<Cheatsheet />}
        />     
    </Routes>
  )
}

export default RouteSwitcher
