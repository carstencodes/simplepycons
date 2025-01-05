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


class LinksysIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "linksys"

    @property
    def original_file_name(self) -> "str":
        return "linksys.svg"

    @property
    def title(self) -> "str":
        return "Linksys"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Linksys</title>
     <path d="M19.871 0c-1.7024 0-3.082 1.38-3.082 3.082 0 1.7025 1.38
 3.08 3.082 3.082 1.7026 0 3.082-1.3795 3.082-3.082
 0-1.7024-1.3795-3.082-3.082-3.082ZM1.047.488V24h21.3105v-3.469H5.166V.488Zm7.156
 0v17.156h14.154v-3.4707h-10.039V.488Z" />
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
