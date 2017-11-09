"""
Tests for schedules.
"""

# pylint: disable=E1129

import unittest

import numpy as np
import tensorflow as tf

from anyrl.algos import LinearTFSchedule

class TestLinearTFSchedule(unittest.TestCase):
    """
    Tests for LinearTFSchedule.
    """
    def test_values(self):
        """
        Test values throughout the schedule.
        """
        with tf.Graph().as_default():
            with tf.Session() as sess:
                sched = LinearTFSchedule(duration=10, start_value=7, end_value=0.5,
                                         dtype=tf.float64)
                sess.run(tf.global_variables_initializer())
                self.assertTrue(np.allclose(sess.run(sched.value), 7))
                sched.add_time(sess, 7.5)
                self.assertTrue(np.allclose(sess.run(sched.value), 2.125))
                for _ in range(3):
                    sched.add_time(sess, 10)
                    self.assertTrue(np.allclose(sess.run(sched.value), 0.5))

if __name__ == '__main__':
    unittest.main()
