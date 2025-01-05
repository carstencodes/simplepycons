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


class ItermTwoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iterm2"

    @property
    def original_file_name(self) -> "str":
        return "iterm2.svg"

    @property
    def title(self) -> "str":
        return "iTerm2"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iTerm2</title>
     <path d="M24 5.359v13.282A5.36 5.36 0 0 1 18.641 24H5.359A5.36
 5.36 0 0 1 0 18.641V5.359A5.36 5.36 0 0 1 5.359 0h13.282A5.36 5.36 0
 0 1 24 5.359m-.932-.233A4.196 4.196 0 0 0 18.874.932H5.126A4.196
 4.196 0 0 0 .932 5.126v13.748a4.196 4.196 0 0 0 4.194
 4.194h13.748a4.196 4.196 0 0 0 4.194-4.194zm-.816.233v13.282a3.613
 3.613 0 0 1-3.611 3.611H5.359a3.613 3.613 0 0
 1-3.611-3.611V5.359a3.613 3.613 0 0 1 3.611-3.611h13.282a3.613 3.613
 0 0 1 3.611 3.611M8.854 4.194v6.495h.962V4.194zM5.483
 9.493v1.085h.597V9.48q.283-.037.508-.133.373-.165.575-.448.208-.284.208-.649a.9.9
 0 0 0-.171-.568 1.4 1.4 0 0 0-.426-.388 3 3 0 0 0-.544-.261 32 32 0 0
 0-.545-.209 1.8 1.8 0 0 1-.426-.216q-.164-.12-.164-.284
 0-.223.179-.351.18-.126.485-.127.344 0
 .575.105.239.105.5.298l.433-.5a2.3 2.3 0 0 0-.605-.433 1.6 1.6 0 0
 0-.582-.159v-.968h-.597v.978a2 2 0 0 0-.477.127 1.2 1.2 0 0
 0-.545.411q-.194.268-.194.634 0 .335.164.56.164.224.418.38a4 4 0 0 0
 .552.262q.291.104.545.209.261.104.425.238a.39.39 0 0 1 .165.321q0
 .225-.187.359-.18.134-.537.134-.381 0-.717-.134a4.4 4.4 0 0
 1-.649-.351l-.388.589q.209.173.477.306.276.135.575.217.191.046.373.064"
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
        return '''https://github.com/gnachman/iTerm2/blob/6a857'''

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
