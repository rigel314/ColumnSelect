import sublime_api, sublime, sublime_plugin, re
import functools

# colSel
# TODO: add:
#			a better interface
#			graceful error handling
#			defalut behavior
class ColSelCommand(sublime_plugin.TextCommand):
	def run(self, edit, col, patt='\s+'):
		newSels = []

		for s in self.view.sel(): # for each selection region
			sel = self.view.substr(s)
			seps = re.findall(patt,sel)
			cols = re.split(patt,sel)
			
			cn = 0
			sn = 0
			start = s.begin()
			tmpCol = col - 1

			if cols[0] == '':
				start += len(seps[sn])
				cn += 1
				tmpCol += 1
				sn += 1

			while cn < tmpCol:
				if cn < len(cols):
					start += len(cols[cn])
				cn += 1
				if sn < len(seps):
					start += len(seps[sn])
				sn += 1
			if cn < len(cols):
				end = start + len(cols[cn])
				newSels.append(sublime.Region(start, end))

		self.view.sel().clear()
		self.view.sel().add_all(newSels)


# class EveryOtherLineCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		x = 0
# 		sels = []
# 		for s in self.view.sel():
# 			x = x + 1
# 			if x%2 == 0:
# 				sels.append(s)
# 		for s in sels:
# 			self.view.sel().subtract(s)
# 		sublime.status_message(str(x))

# class ClickDetector(sublime_plugin.EventListener) :
# 	def on_text_command(self, view, name, args) :
# 		# print(self)
# 		# print(view)
# 		# print(name)
# 		# print(args)
# 		pass
