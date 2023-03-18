from refactor.message import Message, MessagePool
from unittest import TestCase

class TestMessagePool(TestCase):
    def test_message_fully_observable(self):
        message_pool = MessagePool()
        p1_message = Message("player1", "I'm player 1", 1)
        p2_message = Message("player2", "I'm player 2", 1)

        message_pool.append_message(p1_message)
        message_pool.append_message(p2_message)
        p1_observation = message_pool.get_visible_messages("player1", 2)
        assert p1_observation[0].msg_id == p1_message.msg_id
        assert p1_observation[1].msg_id == p2_message.msg_id

    def test_message_by_turn(self):
        message_pool = MessagePool()
        p1_message = Message("player1", "I'm player 1", 1)
        p2_message = Message("player2", "I'm player 2", 2)
        message_pool.append_message(p1_message)
        message_pool.append_message(p2_message)
        p1_observation = message_pool.get_visible_messages("player1", 2)
        assert p1_observation[0].msg_id == p1_message.msg_id
        assert len(p1_observation) == 1

    def test_message_partial_observation(self):
        message_pool = MessagePool()
        p1_message = Message("player1", "I'm player 1", 1)
        p2_message = Message("player2", "I'm player 2", 1, visible_to=["player2"])

        message_pool.append_message(p1_message)
        message_pool.append_message(p2_message)
        p1_observation = message_pool.get_visible_messages("player1", 2)
        p2_observation = message_pool.get_visible_messages("player2", 2)
        assert len(p1_observation) == 1
        assert len(p2_observation) == 2

