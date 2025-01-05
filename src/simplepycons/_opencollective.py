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


class OpenCollectiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opencollective"

    @property
    def original_file_name(self) -> "str":
        return "opencollective.svg"

    @property
    def title(self) -> "str":
        return "Open Collective"

    @property
    def primary_color(self) -> "str":
        return "#7FADF2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open Collective</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12c2.54 0
 4.894-.79 6.834-2.135l-3.107-3.109a7.715 7.715 0 1 1
 0-13.512l3.107-3.109A11.943 11.943 0 0 0 12 0zm9.865 5.166l-3.109
 3.107A7.67 7.67 0 0 1 19.715 12a7.682 7.682 0 0 1-.959 3.727l3.109
 3.107A11.943 11.943 0 0 0 24 12c0-2.54-.79-4.894-2.135-6.834z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://docs.opencollective.com/help/about#me'''

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
