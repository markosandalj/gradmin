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
          {/* <Route exact path="/index/problems/fizika/matura/:id">
            <ProblemsByMaturaList></ProblemsByMaturaList>
          </Route> */}
          {/* <Route exact path="/index/problems/fizika/matura/:id/print">
            <ProblemsByMaturaPrint></ProblemsByMaturaPrint>
          </Route> */}
          {/* <Route exact path="/index/skripta/:subject/:level">
            <SkriptaSections></SkriptaSections>
          </Route> */}
          {/* <Route exact path="/index/skripta/:subject/:level/:id">
            <Skripta></Skripta>
          </Route> */}
        </Switch>
      </Frame>
    </Router>   
    </AppProvider>
  )
}