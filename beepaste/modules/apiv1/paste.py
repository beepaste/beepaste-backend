import datetime
from SanicMongo import Document
from SanicMongo.fields import (IntField, DateTimeField, StringField, URLField,
                                BooleanField)
import json

validEncriptions = {'no', 'pgp', 'passwd'}
validSyntax = {'abap', 'abc', 'actionscript', 'ada', 'apache_conf', 'applescript',
               'asciidoc', 'assembly_x86', 'autohotkey', 'batchfile', 'c9search',
               'c_cpp', 'cirru', 'clojure', 'cobol', 'coffee', 'coldfusion',
               'csharp', 'css', 'curly', 'd', 'dart', 'diff', 'django', 'dockerfile',
               'dot', 'eiffel', 'ejs', 'elixir', 'elm', 'erlang', 'forth', 'ftl',
               'gcode', 'gherkin', 'gitignore', 'glsl', 'golang', 'groovy', 'haml',
               'handlebars', 'haskell', 'haxe', 'html', 'html_elixir', 'html_ruby', 'ini',
               'io', 'jack', 'jade', 'java', 'javascript', 'json', 'jsoniq', 'jsp',
               'jsx', 'julia', 'latex', 'lean', 'less', 'liquid', 'lisp', 'live_script',
               'livescript', 'logiql', 'lsl', 'lua', 'luapage', 'lucene', 'makefile',
               'markdown', 'mask', 'matlab', 'maze', 'mel', 'mips_assembler',
               'mipsassembler', 'mushcode', 'mysql', 'nix', 'objectivec', 'ocaml',
               'pascal', 'perl', 'pgsql', 'php', 'plain_text', 'powershell',
               'praat', 'prolog', 'properties', 'protobuf', 'python', 'r', 'rdoc',
               'rhtml', 'ruby', 'rust', 'sass', 'scad', 'scala', 'scheme', 'scss',
               'sh', 'sjs', 'smarty', 'snippets', 'soy_template', 'space', 'sql',
               'sqlserver', 'stylus', 'svg', 'swift', 'swig', 'tcl', 'tex', 'text',
               'textile', 'toml', 'twig', 'typescript', 'vala', 'vbscript', 'velocity',
               'verilog', 'vhdl', 'xml', 'xquery', 'yaml'}

class Paste(Document):
    """
    The PASTE class have attributes for a paste such as raw text (encoded in Base64),
    pasteDate and expiretDate and so on! This class is developing.
    """

    author = StringField(default="Anonymous", max_length=127)
    title = StringField(default="Untitled", max_length=127)
    shorturl = URLField(default="https://beepaste.io/")

    date = DateTimeField(default=datetime.datetime.utcnow())
    expiryDate = DateTimeField(default=datetime.datetime.utcnow())
    toExpire = BooleanField(default=False)

    raw = StringField(required=True)
    encryption = StringField(choices=validEncriptions, default="no")
    syntax = StringField(choices=validSyntax, default="text")

    views = IntField(default=0)
    ownerID = IntField(default=0)

    meta = {'collection': 'pastes'}
