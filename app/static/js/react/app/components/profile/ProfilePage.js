import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import Greeting from './Greeting';
import { Link } from 'react-router-dom';
import Connections from "../connections/Connections";

class ProfilePage extends React.Component {
  fetchUserData(userID) {
    fetch(`/api/user/${userID}`)
    .then(response => response.json())
    .then(data => this.setState(data))
  }

  constructor(props) {
    super(props);
    this.userID = this.props.match.params.number;
  }

  componentDidMount() {
    this.fetchUserData(this.props.match.params.number)
  }

  componentWillReceiveProps(nextProps) {
    this.userID = nextProps.match.params.number;
    this.fetchUserData(this.userID)
  }

  render() {
    return (
      <div>
        <Greeting userID={this.userID} userDetails={this.state} />
        <Link to={`/profile/${parseInt(this.userID) + 1}`}>Next user</Link>
        <Connections userID={this.userID} userDetails={this.state} />
      </div>
    )
  }
}

ProfilePage.propTypes = {
  filter: PropTypes.string,
  onFilter: PropTypes.func,
  match: PropTypes.shape({
    params: PropTypes.shape({
      number: PropTypes.string
    })
  })
};

const mapStateToProps = (state) => {
  return {
    filter: state.filter
  };
};


export default connect(
  mapStateToProps,
)(ProfilePage);
