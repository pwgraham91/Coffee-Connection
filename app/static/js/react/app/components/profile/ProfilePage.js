import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';
import Greeting from './Greeting';
import { Link } from 'react-router-dom';

class ProfilePage extends React.Component {
  fetchUserData(userID) {
    fetch(`/api/user/${userID}`)
    .then(response => response.json())
    .then(data => this.setState(data))
  }

  componentDidMount() {
    this.fetchUserData(this.props.match.params.number)
  }

  componentWillReceiveProps(nextProps) {
    this.fetchUserData(nextProps.match.params.number)
  }

  render() {
    return (
      <div>
        <Greeting userID={this.props.match.params.number} userDetails={this.state} />
        <Link to={`/profile/${parseInt(this.props.match.params.number) + 1}`}>Next user</Link>
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
