import React from 'react';
import QueueAnim from 'rc-queue-anim';
import { Link, Redirect } from 'react-router-dom';
import { login, isAuthenticate } from '../../_service'
import { Button, Form, Input, Row, Col, Layout, Typography, Divider, message } from 'antd';
import { IdcardOutlined, KeyOutlined } from '@ant-design/icons';
import './auth.css'

const { Content } = Layout
const { Title } = Typography

class LoginForm extends React.Component{
	state = {
		not_match : false,
		checking: false,
		success: false
	}

	onFinish = (data) =>{
		this.setState({not_match: false, checking: true})
		login(data.email, data.password)		//	login
		.then(resp => {
			this.setState({checking: false, success: resp.success})
			this.props.history.push('/')
		})
		.catch(error => {
			if(error === 'Server error !'){
				this.setState({checking: false})
			} else {
				this.setState({not_match: true, checking: false})
			}
			message.error(error, 3);
		})
	}

	render(){
		if (isAuthenticate()){
			return <Redirect to='/' />
		}
		return(
			<React.Fragment>
				<Layout className="container">
					<Content className="auth-content">
						<Row>
							<Col offset={14}>
								<QueueAnim
									animConfig={[
										{ opacity: [1, 0], translateY: [0, 100] },
										{ opacity: [1, 0], translateY: [0, -70] }
									]}
								>
									<div className={`auth-form ${this.state.not_match?'auth-form-error':this.state.success?'auth-form-success':''}`} key="form">
										<Title level={2} className="goto-campus">Goto Campus</Title>
										<Divider className={`${this.state.not_match?'divider-error':this.state.success?'divider-success':'divider'}`} />

										<Form name="normal_login" className="login-form" onFinish={this.onFinish}>
										
											<Form.Item
												name="email"
												rules={[
													{required: true, message: 'Please write your Email!'},
													{type: 'email', message: 'Invalid Email address'}
												]}
											>
												<Input
													placeholder="Email"
													size="large"
													className="input"
													prefix={<IdcardOutlined />}
												/>
											</Form.Item>

											<Form.Item
												name="password"
												rules={[{required: true, message: 'Please write your Password!'}]}
											>
												<Input.Password
													placeholder="Password"
													size="large"
													className="input"
													prefix={<KeyOutlined />}
												/>
											</Form.Item>

											<Form.Item>
												<Button htmlType="submit" type='primary' shape="circle" className="submit">Go</Button>
											</Form.Item>
											<Link to="/register" className="link">Admit Now</Link>
										</Form>
									</div>
								</QueueAnim>
							</Col>
						</Row>
					</Content>
				</Layout>
			</React.Fragment>
		)
	}
}

export { LoginForm };
