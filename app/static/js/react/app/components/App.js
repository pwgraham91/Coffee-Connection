import React from 'react';
import { Link } from 'react-router-dom';
import Routes from '../routes';
import Navigation from "./Navigation";

const App = () =>
    <div>
        <Navigation/>
        { Routes }
    </div>;

export default App;
