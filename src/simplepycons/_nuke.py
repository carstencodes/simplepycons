#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class NukeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nuke"

    @property
    def original_file_name(self) -> "str":
        return "nuke.svg"

    @property
    def title(self) -> "str":
        return "Nuke"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nuke</title>
     <path d="M12.293.004c6.625.162 11.865 5.664 11.703 12.29-.162
 6.625-5.664 11.865-12.29 11.703C5.081 23.835-.159 18.333.003
 11.707l.001-.025C.18 5.066 5.678-.158 12.293.004zm0
 1.238c-5.941-.164-10.89 4.52-11.054 10.461s4.52 10.89 10.461
 11.054c5.941.164 10.89-4.52
 11.054-10.461l.001-.025c.15-5.932-4.53-10.866-10.462-11.029zm5.842
 8.302h2.4c.976 0 .682-.873.682-.873a9.587 9.587 0 0
 0-2.111-3.431l-.005.011a10.052 10.052 0 0 0-3.355-2.329.612.612 0 0
 0-.894.622c-.044.802-.142 2.395-.142
 2.395s.016.769-.627.769c-.813.011-1.489-.044-1.489-.044a2.314 2.314 0
 0 1-1.255-.545L8.868 3.511a1.09 1.09 0 0 0-1.407-.196 9.758 9.758 0 0
 0-4.713 5.384c-.256.714.333.806.731.806h6a2.086 2.086 0 0 1
 1.68.627c.785.824 1.331 1.369 1.331 1.369s.48.54 1.26
 1.358c.431.459.632 1.089.545 1.713 0 0-.295 5.744-.295
 6-.027.398.038.993.769.775a9.756 9.756 0 0 0 5.618-4.424 1.091 1.091
 0 0 0-.12-1.418l-2.471-2.607a2.303 2.303 0 0
 1-.496-1.282s-.022-.682.033-1.489c.044-.643.802-.583.802-.583zm-2.362
 1.374c-.475.469-1.484.229-2.22-.545-.736-.775-.924-1.801-.45-2.254.475-.453
 1.502-.239 2.239.536.737.774.906 1.794.431 2.263z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
