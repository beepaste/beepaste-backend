import datetime

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


class Paste(object):
    """
    The PASTE class have attributes for a paste such as raw text (encoded in Base64),
    pasteDate and expiretDate and so on! This class is developing.
    """
    def __init__(self, author="Anonymous", title="Untitled",
                 date=datetime.datetime.utcnow(), expiretDate=datetime.datetime.utcnow(),
                 toExpire=False, raw="", encryption="no", syntax="text", views=0,
                 ownerID=0):
        self.author = author  # paste author name!
        self.title = title  # paste title!
        self.date = date  # paste submission date!
        self.expiretDate = expiretDate  # paste expiration date (equals paste
                                        # submission date if toExpire=False)
        self.toExpire = toExpire  # if paste has to be expired!
        self.raw = raw  # paste raw text encoded in Base64!
        self.encryption = encryption  # paste encryption method (either
                                      # 'no', 'pgp' or 'passwd')
        self.syntax = syntax  # paste syntax highlighting!
        self.views = views  # paste views count!
        self.ownerID = ownerID  # paste owner id! if 0, haven't owner otherwise
                                # equals to id of the owner username! it will
                                # override author :)
        self.validate()

    def validate(self):
        assert type(self.author) == str
        assert len(self.author) > 0 and len(self.author) < 63

        assert type(self.title) == str
        assert len(self.title) > 0 and len(self.title) < 255

        assert type(self.date) == datetime.datetime
        assert type(self.expiretDate) == datetime.datetime

        assert type(self.raw) == str
        assert len(self.raw) > 0

        assert self.encryption in validEncriptions

        assert self.syntax in validSyntax

        assert type(self.views) == int
        assert self.views >= 0

        assert type(self.ownerID) == int
        assert self.ownerID >= 0
