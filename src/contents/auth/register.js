import React from 'react';
import QueueAnim from 'rc-queue-anim';
import { Link } from 'react-router-dom';
import { Button, Form, Input, Row, Col, Layout, Typography, Divider, Select } from 'antd';
import { IdcardOutlined, LockOutlined } from '@ant-design/icons';
import './auth.css'

const { Content } = Layout
const { Title } = Typography

class SignupForm extends React.Component{
    state = {
        form_show: true,
        not_match: false,
        success: false,
        loading: false
    }

    onFinish = () =>{
        return
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
                                        { opacity: [1, 0], translateY: [0, 60] },
                                        { opacity: [1, 0], translateY: [0, -60] }
                                    ]}
                                >
                                    {
                                        this.state.form_show ? 
                                            <div className={`auth-form ${this.state.not_match?'auth-form-error':this.state.success?'auth-form-success':''}`} key="form">
                                            <Title level={2} className="goto-campus">Register</Title>
                                            <Divider className={`${this.state.not_match?'divider-error':this.state.success?'divider-success':'divider'}`} />
                                            <Form name="normal_login" className="login-form" onFinish={this.onFinish}>

                                                <Form.Item style={{margin:0}}>
                                                    <Form.Item
                                                        name="first_name"
                                                        style={{ display: 'inline-block', width: 'calc(50% - 8px)', marginRight: '8px'}}
                                                        rules={[{required: true, message: 'Please Write your First Name!'}]}
                                                        validateStatus={this.state.not_match?'error':''}
                                                    >
                                                        <Input 
                                                            placeholder="First Name" 
                                                            className="input"
                                                        />
                                                    </Form.Item>
                                                    <Form.Item
                                                        name="last_name"
                                                        style={{ display: 'inline-block', width: 'calc(50% - 8px)', marginLeft: '8px'}}
                                                        rules={[{required: true, message: 'Please write your Last Name!'}]}
                                                    >
                                                        <Input 
                                                            placeholder="Last Name" 
                                                            className="input"
                                                        />
                                                    </Form.Item>
                                                </Form.Item>

                                                <Form.Item name="email" rules={[{required: true, message: 'Please input your Email Address!'}]}>
                                                    <Input 
                                                        placeholder="Email" 
                                                        className="input"
                                                        allowClear
                                                        prefix={<IdcardOutlined />}
                                                    />
                                                </Form.Item>

                                                <Form.Item name="i_am" rules={[{required: true, message: 'Please select your Gender!'}]}>
                                                    <Select 
                                                        placeholder="I am" 
                                                        onChange={this.onGenderChange}
                                                        allowClear
                                                        prefix={<IdcardOutlined />}
                                                    >
                                                    <Select.Option value="Teacher">Teacher</Select.Option>
                                                    <Select.Option value="Student">Student</Select.Option>
                                                    <Select.Option value="Staff">Staff</Select.Option>
                                                    </Select>
                                                </Form.Item>

                                                <Form.Item name="password1" rules={[{required: true, message: 'Please write your Password!'}]}>
                                                    <Input.Password
                                                        placeholder="Password"
                                                        className="input"
                                                        prefix={<LockOutlined />}
                                                    />
                                                </Form.Item>

                                                <Form.Item name="password2" rules={[{required: true, message: 'Please write your Password again!'}]}>
                                                    <Input.Password
                                                        placeholder="Confirm Password"
                                                        className="input"
                                                        prefix={<LockOutlined />}
                                                    />
                                                </Form.Item>

                                                <Form.Item>
                                                    <Button htmlType="submit" type='primary' shape="circle" className="submit">Submit</Button>
                                                </Form.Item>
                                                <Link to='/login' className="link" onClick={()=>this.setState({form_show: false})}>Already a member?</Link>
                                            </Form>
                                        </div> 
                                        : null
                                    }
                                    
                                </QueueAnim>
                            </Col>
                        </Row>
                    </Content>
                </Layout>
            </React.Fragment>
        )
    }
}

export default SignupForm;
