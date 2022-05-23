// REACT & REDUX
import React, { Component, useState, useEffect, useCallback } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import { useParams } from 'react-router';

// SHOPIFY
import { AppProvider, Frame, TopBar } from '@shopify/polaris';

// COMPONENTS
import Header from "./layout/Header";
import Sidebar from "./layout/Sidebar";
import Skripta from "./pages/Skripta";
import SkriptaSections from "./pages/SkriptaSections";
import MaturaList from "./pages/MaturaList";
import MaturaProblems from "./pages/MaturaProblems";
import ProblemsImporter from "./pages/ProblemsImporter";
import CheatsheetsList from "./pages/CheatsheetsList";
import CheatsheetPage from "./pages/CheatsheetPage";

export default function App() {
  const [mobileNavigationActive, setMobileNavigationActive] = useState(false);

  const toggleMobileNavigationActive = useCallback(
    () =>
      setMobileNavigationActive(
        (mobileNavigationActive) => !mobileNavigationActive,
      ),
    [],
  );

  const navigationMarkup = (
    <Sidebar></Sidebar>
  );

  const topBarMarkup = (
    // <Header></Header>
    <TopBar
      showNavigationToggle
      onNavigationToggle={toggleMobileNavigationActive}
    />
  )

  return (
    <AppProvider
      i18n={{
      }}
    >
    <Router>
      <Frame 
        navigation={navigationMarkup}
        topBar={topBarMarkup}
        showMobileNavigation={mobileNavigationActive}
        onNavigationDismiss={toggleMobileNavigationActive}
      >
        <Switch >
          <Route exact path="/index">
          </Route>
          <Route exact path="/index/skripta/:skripta_id/list">
            <SkriptaSections></SkriptaSections>
          </Route>
          <Route exact path="/index/skripta/:skripta_id">
            <Skripta></Skripta>
          </Route>
          <Route exact path="/index/skripta/:skripta_id/:section_id/:section_order">
            <Skripta></Skripta>
          </Route>
          <Route exact path="/index/matura/:subject_id/list">
            <MaturaList></MaturaList>
          </Route>
          <Route exact path="/index/matura/:matura_id">
            <MaturaProblems></MaturaProblems>
          </Route>
          <Route exact path="/index/problems_importer">
            <ProblemsImporter></ProblemsImporter>
          </Route>
          <Route exact path="/index/cheatsheets/list">
            <CheatsheetsList />          
          </Route>
          <Route exact path="/index/cheatsheets/:cheatsheet_id">
            <CheatsheetPage/>          
          </Route>
        </Switch>
      </Frame>
    </Router>   
    </AppProvider>
  )
}