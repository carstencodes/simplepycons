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


class SourcehutIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sourcehut"

    @property
    def original_file_name(self) -> "str":
        return "sourcehut.svg"

    @property
    def title(self) -> "str":
        return "SourceHut"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SourceHut</title>
     <path d="M12 0C5.371 0 0 5.371 0 12s5.371 12 12 12 12-5.371
 12-12S18.629 0 12 0Zm0 21.677A9.675 9.675 0 0 1 2.323 12 9.675 9.675
 0 0 1 12 2.323 9.675 9.675 0 0 1 21.677 12 9.675 9.675 0 0 1 12
 21.677Z" />
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
