import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';


class Navigation extends React.Component {
  render() {
    return (
      <div>
        <AppBar position="static">
          <Toolbar>
            <Link to={'/'} style={{
              flex: 1
            }}>
              <Typography variant="title" color="inherit" style={{
                color: 'white'
              }}>
                FloSports Coffee Connection
              </Typography>
            </Link>
            <Button color="inherit">Login</Button>
          </Toolbar>
        </AppBar>
      </div>
    )
  }
}

export default Navigation;
