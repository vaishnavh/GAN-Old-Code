'''
                session.run([self.grad_d_2], {
                    self.x: np.reshape(x, (self.batch_size, 1)),
                    self.z: np.reshape(z, (self.batch_size, 1))
                })
                # loss_d is the loss returned by running one minibatch update step. 
                # it is retreived because we want to print it

                loss_d, _ = session.run([loss_d,self.apply_grad_d])
'''
                # update generator

'''
                session.run([self.opt_g_2], {
                    self.z: np.reshape(z, (self.batch_size, 1))
                })
                loss_g, _ = session.run([loss_g,self.apply_grad_g])
'''