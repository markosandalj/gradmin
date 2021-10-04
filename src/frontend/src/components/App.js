// REACT & REDUX
import React, { Component, useState, useEffect } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";

// SHOPIFY
import { AppProvider, Frame } from '@shopify/polaris';

// COMPONENTS
import Header from "./layout/Header";
import ProblemsByMaturaList from "./pages/ProblemsByMatura";
import ProblemsByMaturaPrint from "./pages/ProblemsByMaturaPrint";
import Sidebar from "./layout/Sidebar";
import Skripta from "./pages/Skripta";
import SkriptaSections from "./pages/SkriptaSections";
import HomePage from './pages/HomePage';
import MaturaList from "./pages/MaturaList";
import MaturaProblems from "./pages/MaturaProblems";

export default function App() {
  const navigationMarkup = (
    <Sidebar></Sidebar>
  );

  const topBarMarkup = (
    <Header></Header>
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
          <Route exact path="/index/skripta/:skripta_id/:section_id">
            <Skripta></Skripta>
          </Route>
          <Route exact path="/index/matura/:subject_id/list">
            <MaturaList></MaturaList>
          </Route>
          <Route exact path="/index/matura/:matura_id">
            <MaturaProblems></MaturaProblems>
          </Route>
        </Switch>
      </Frame>
    </Router>   
    </AppProvider>
  )
}