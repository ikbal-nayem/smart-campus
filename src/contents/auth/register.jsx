import React from 'react';
import QueueAnim from 'rc-queue-anim';
import { Link, Redirect } from 'react-router-dom';
import { signup, isAuthenticate } from '../../_service'
import { Button, Form, Input, Row, Col, Layout, Typography, Divider, Select, message, Alert } from 'antd';
import { LockOutlined } from '@ant-design/icons';
import './auth.css'

const { Content } = Layout
const { Title } = Typography

class SignupForm extends React.Component{
    state = {
        form_show: true,
        error: false,
        success: false,
        loading: false,
        error_msg: null
    }

    onFinish = async (data) =>{
        this.setState({loading: true, error: false})
        signup(data)
        .then(resp => {
            if(resp.success){
                message.success('Account created successfully!')
                this.setState({success: true, loading: false, form_show: false})
                this.props.history.push('/')
            }
        })
        .catch(error => {
            this.setState({loading: false, error: true, error_msg: error.error})
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
                                        { opacity: [1, 0], translateY: [0, 60] },
                                        { opacity: [1, 0], translateY: [0, -60] }
                                    ]}
                                >
                                    {
                                        this.state.form_show ? 
                                            <div className={`auth-form ${this.state.error?'auth-form-error':this.state.success?'auth-form-success':''}`} key="form">
                                            <Title level={2} className="goto-campus">Admit</Title>
                                            <Divider className={`${this.state.error?'divider-error':this.state.success?'divider-success':'divider'}`} />
                                            {
                                                this.state.error_msg ? 
                                                <Alert message={`${this.state.error_msg}`} type="error" showIcon closable style={{marginBottom:10}} /> : null
                                            }
                                            <Form name="normal_login" className="login-form" onFinish={this.onFinish}>

                                                <Form.Item style={{margin:0}}>
                                                    <Form.Item name="first_name"
                                                        style={{ display: 'inline-block', width: 'calc(50% - 8px)', marginRight: '8px'}}
                                                        rules={[{required: true, message: 'Please fill this field!'}]}
                                                    >
                                                        <Input 
                                                            placeholder="First Name" 
                                                            className="input"
                                                        />
                                                    </Form.Item>
                                                    <Form.Item name="last_name"
                                                        style={{ display: 'inline-block', width: 'calc(50% - 8px)', marginLeft: '8px'}}
                                                        rules={[{required: true, message: 'Please fill this field!'}]}
                                                    >
                                                        <Input 
                                                            placeholder="Last Name" 
                                                            className="input"
                                                        />
                                                    </Form.Item>
                                                </Form.Item>

                                                <Form.Item name="email"
                                                    rules={[
                                                        {required: true, message: 'Please fill this field!'},
                                                        {type: 'email', message: 'Invalid Email address!'}
                                                    ]}
                                                >
                                                    <Input 
                                                        placeholder="Email" 
                                                        className="input"
                                                        allowClear
                                                    />
                                                </Form.Item>

                                                <Form.Item name="i_am" rules={[{required: true, message: 'Please select your Gender!'}]}>
                                                    <Select placeholder="I am">
                                                        <Select.Option value="teacher">Teacher</Select.Option>
                                                        <Select.Option value="student">Student</Select.Option>
                                                        <Select.Option value="staff">Staff</Select.Option>
                                                    </Select>
                                                </Form.Item>

                                                <Form.Item name="password1"
                                                    hasFeedback
                                                    rules={[
                                                        {required: true, message: 'Please create a strong password'},
                                                        {min: 8, message: 'Password should be 8 character or above.'}
                                                    ]}
                                                >
                                                    <Input.Password
                                                        placeholder="Password"
                                                        className="input"
                                                        prefix={<LockOutlined />}
                                                    />
                                                </Form.Item>

                                                <Form.Item name="password2"
                                                    hasFeedback
                                                    dependencies={['password1']}
                                                    rules={[
                                                        {required: true, message: 'Please write your Password again!'},
                                                        ({ getFieldValue }) => ({
                                                            validator(_, value) {
                                                            if (!value || getFieldValue('password1') === value) {
                                                                return Promise.resolve();
                                                            }
                                                            return Promise.reject('Passwords that you entered do not match!');
                                                            },
                                                        }),
                                                    ]}
                                                >
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

export { SignupForm };
