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


class ProtodotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "protodotio"

    @property
    def original_file_name(self) -> "str":
        return "protodotio.svg"

    @property
    def title(self) -> "str":
        return "Proto.io"

    @property
    def primary_color(self) -> "str":
        return "#34A7C1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Proto.io</title>
     <path d="M12 11.997c-.728 0-1.316-.59-1.316-1.317S11.272 9.363 12
 9.363s1.316.589 1.316 1.316-.588 1.318-1.316
 1.318zm2.916-.021c0-2.828-1.109-5.397-2.916-7.298-1.807 1.9-2.916
 4.47-2.916 7.298 0 1.297.234 2.535.66 3.683-.618.9-1.074 2.16-1.275
 3.616.639-.767 1.422-1.306 2.292-1.591.363.555.78 1.096 1.239
 1.574.461-.494.876-1.02 1.239-1.59.87.271 1.653.826 2.29
 1.576-.199-1.456-.655-2.716-1.275-3.615.427-1.155.66-2.385.66-3.69l.002.037zM12
 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10
 10zm0-22C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627 0
 12 0z" />
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
