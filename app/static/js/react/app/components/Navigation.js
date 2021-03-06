import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';


class Navigation extends React.Component {
  rightSideButtons() {
    if (window.user) {
      return (
        <div>
          <Link to={`/profile/${window.user.id}`}><Button style={{
            color: 'white'
          }}>{ window.user.name }</Button></Link>
          <a href="/logout">
            <Button style={{
              color: 'white'
            }}>Logout</Button>
          </a>
        </div>
      )
    } else {
      return (
        <a href={window.authUrl}><Button style={{
          color: 'white'
        }}>Login</Button></a>
      )
    }
  }

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
            {this.rightSideButtons()}
          </Toolbar>
        </AppBar>
      </div>
    )
  }
}

export default Navigation;
