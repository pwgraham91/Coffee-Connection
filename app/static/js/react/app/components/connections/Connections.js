import PropTypes from 'prop-types';
import React from 'react';
import ExistingConnections from "./ExistingConnections";
import GenerateConnections from "./GenerateConnections";
import {isCurrentUser} from "../../lib/user";

export default class Connections extends React.Component {
  showGenerateConnections() {
    if (isCurrentUser(this.props.userID) && window.user.admin) {
      return (
        <GenerateConnections userID={this.props.userID} userDetails={this.props.userDetails} />
      )
    }
  }
  render() {
    return (
      <div>
        <h2>Connections</h2>
        {this.showGenerateConnections()}
        <ExistingConnections userID={this.props.userID} userDetails={this.props.userDetails} />
      </div>
    )
  }
}

Connections.propTypes = {
  userID: PropTypes.string,
  userDetails: PropTypes.object
};

