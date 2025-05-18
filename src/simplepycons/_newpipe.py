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


class NewpipeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "newpipe"

    @property
    def original_file_name(self) -> "str":
        return "newpipe.svg"

    @property
    def title(self) -> "str":
        return "NewPipe"

    @property
    def primary_color(self) -> "str":
        return "#CD201F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NewPipe</title>
     <path d="M11.988 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.012 0zm-4.38 4.608s1.512.888
 3.672 2.16C13.848 8.28 17.304 10.32 20.16 12a5976.548 5976.548 0 0
 0-8.736 5.16v-2.675c1.07-.63 2.467-1.455
 4.224-2.485-1.296-.768-2.856-1.703-4.032-2.375l-1.68-.985v9.399l-2.328
 1.377z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/TeamNewPipe/NewPipe/blob/f'''

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
