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


class TestcafeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "testcafe"

    @property
    def original_file_name(self) -> "str":
        return "testcafe.svg"

    @property
    def title(self) -> "str":
        return "TestCafe"

    @property
    def primary_color(self) -> "str":
        return "#36B6E5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TestCafe</title>
     <path d="m20.315 4.319-8.69 8.719-3.31-3.322-2.069 2.076 5.379
 5.398 10.76-10.796zM5.849 14.689 0
 19.682h24l-5.864-4.991h-3.2l-1.024.896h3.584l3.072
 2.815H3.417l3.072-2.815h2.688l-.896-.896z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/DevExpress/testcafe/blob/d
d174b6682b5f2675ac90e305d3d893c36a1d814/media/logos/svg/TestCafe-logo-'''

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
