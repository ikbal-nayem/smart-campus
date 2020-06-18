import React from 'react';
import axios from 'axios';
import QueueAnim from 'rc-queue-anim';
import { Link } from 'react-router-dom';
import { Button, Form, Input, Row, Col, Layout, Typography, Divider } from 'antd';
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
        axios.post(
            "http://localhost:8000/api/account/auth-token/",
            {"username": data.email, "password": data.password}
        ).then(resp => {
            console.log(resp)
            this.setState({not_match: false, checking: false, success: true})
        }).catch(error => {
            if (error.response && error.response.status === 400){
                this.setState({not_match: true, checking: false})
            }
        })
    }
    render(){
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
                                                rules={[{required: true, message: 'Please input your Email Address!'}]}
                                                hasFeedback
                                                validateStatus={this.state.not_match?'error':''}
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
                                                rules={[{required: true, message: 'Please input your Password!'}]}
                                                hasFeedback
                                                validateStatus={this.state.not_match?'error':''}
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

export default LoginForm;
