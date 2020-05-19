import wx
import os
import sys

class SampleClass(wx.Frame):
    def __init__(self, parent, title):
        window_size_x = 600
        window_size_y = 400
        super(SampleClass, self).__init__(parent, title = title, size = (window_size_x, window_size_y))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        layout = [
            [
                {
                    'name' : 'test_label1',
                    'type' : 'label',
                    'length' : 1,
                    'label' : 'test_label1'
                },
                {
                    'name' : 'test_text',
                    'type' : 'text',
                    'length' : 2,
                    'label' : 'test_text1'
                },
                {
                    'name' : 'test_button',
                    'type' : 'button',
                    'length' : 1,
                    'function' : 'call_method',
                    'label' : 'メソッド呼び出し'
                }
            ],
            [
                {
                    'name' : 'test_combobox',
                    'type' : 'combobox',
                    'length' : 2,
                    'list' : ['abc', 'def', 'ghi'],
                    'label' : 'combobox'
                }
            ]
        ]

        parts = {}

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(10, 10)
        for y, row in enumerate(layout):
            for x, col in enumerate(row):
                # partsに同じ名前がすでに登録されてたらエラーする
                if parts.get(col['name']) != None:
                    print('同じKeyが登録されています!!!')
                    exit()
                if col['type'] == 'label':
                    parts[col['name']] = wx.StaticText(panel, wx.ID_ANY, col['label'])
                    sizer.Add(
                        parts[col['name']],
                        pos = (y, x)
                    )
                elif col['type'] == 'text':
                    parts[col['name']] = wx.TextCtrl(panel, wx.ID_ANY, col['label'])
                    sizer.Add(
                        parts[col['name']],
                        pos = (y, x)
                    )
                elif col['type'] == 'button':
                    parts[col['name']] = wx.Button(panel, wx.ID_ANY, label=col['label'])
                    parts[col['name']].Bind(wx.EVT_BUTTON, eval('self.' + col['function']))
                    sizer.Add(
                        parts[col['name']],
                        pos = (y, x)
                    )
                elif col['type'] == 'combobox':
                    parts[col['name']] = wx.ComboBox(panel, wx.ID_ANY, col['label'], choices=col['list'], style=wx.CB_DROPDOWN)
                    sizer.Add(
                        parts[col['name']],
                        pos = (y, x)
                    )

        panel.SetSizerAndFit(sizer)

    def call_method(self, event):
        print(sys._getframe().f_code.co_name)

app = wx.App()
SampleClass(None, title = 'SampleClass')
app.MainLoop()