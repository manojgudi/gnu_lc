#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Jul 11 23:58:22 2013
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 320

		##################################################
		# Blocks
		##################################################
		self.gr_vector_sink_x_0 = gr.vector_sink_f(1)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_float*1, samp_rate)
		self.gr_file_source_0 = gr.file_source(gr.sizeof_float*1, "/home/aviral/trial2.txt", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_file_source_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.gr_vector_sink_x_0, 0))
		print self.gr_vector_sink_x_0.data()
		

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.gr_throttle_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

