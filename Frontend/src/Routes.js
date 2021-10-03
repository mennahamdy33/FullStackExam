
import React from 'react';
import {BrowserRouter, Route, Switch } from "react-router-dom";
import Table from './containers/table';
import Login from "./containers/login"
export default function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route exact path="/login">
                    <Login />
                </Route>
            </Switch>
            <Switch>
                <Route exact path="/table">
                    <Table />
                </Route>
            </Switch>

        </BrowserRouter>
    );
}