import PropTypes from 'prop-types';
import React from 'react';
import ExistingConnections from "./ExistingConnections";
import GenerateConnections from "./GenerateConnections";
import {isCurrentUser} from "../../lib/user";

export default class Connections extends React.Component {
  constructor(props) {
    super(props);
    this.handleGeneration = this.handleGeneration.bind(this)
  }

  showGenerateConnections() {
    if (isCurrentUser(this.props.userID) && window.user.admin) {
      return (
        <GenerateConnections userDetails={this.userDetails} onGeneration={this.handleGeneration} />
      )
    }
  }

  handleGeneration(userDetails) {
    this.setState(userDetails)
  }

  setUserDetailsProps(userDetails) {
    if (userDetails) {
      this.setState(userDetails)
    } else {
      this.setState({
        connections: []
      })
    }
  }

  componentDidMount() {
    this.setUserDetailsProps(this.props.userDetails)
  }

  componentWillReceiveProps(nextProps) {
    this.setUserDetailsProps(nextProps.userDetails)
  }

  render() {
    console.log('current state', this.state)
    return (
      <div>
        <h2>Connections</h2>
        {this.showGenerateConnections()}
        <ExistingConnections userDetails={this.state} />
      </div>
    )
  }
}

Connections.propTypes = {
  userID: PropTypes.string,
  userDetails: PropTypes.object
};
