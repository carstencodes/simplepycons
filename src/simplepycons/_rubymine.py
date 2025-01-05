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


class RubymineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rubymine"

    @property
    def original_file_name(self) -> "str":
        return "rubymine.svg"

    @property
    def title(self) -> "str":
        return "RubyMine"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RubyMine</title>
     <path d="M0 0v24h24V0Zm3.056 3H6.92q.945 0
 1.665.347t1.106.977c.262.42.392.902.392 1.46q0 .835-.399 1.478a2.6
 2.6 0 0 1-1.125.99 2 2 0 0 1-.297.103q-.066.02-.13.04L10.276
 12H8.264l-1.94-3.4H4.811V12H3.056Zm8.51 0h2.444l1.851
 5.907.154.773.136-.773L17.937 3h2.482v9h-1.736V5.578l.026-.47L16.613
 12H15.34l-2.07-6.846.026.424V12h-1.73ZM4.812
 4.459V7.14h1.993q.444-.001.771-.161.335-.167.515-.47c.12-.205.18-.439.18-.713q0-.411-.18-.707a1.17
 1.17 0 0 0-.515-.462 1.7 1.7 0 0 0-.77-.168ZM2.996 19.2h9.6V21h-9.6z"
 />
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
