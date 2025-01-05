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


class SteemIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "steem"

    @property
    def original_file_name(self) -> "str":
        return "steem.svg"

    @property
    def title(self) -> "str":
        return "Steem"

    @property
    def primary_color(self) -> "str":
        return "#171FC9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Steem</title>
     <path d="M17.683
 16.148l-.114.114c-.235.236-.486.46-.748.666l-.298.235a.11.11 0
 01-.176-.11l.12-.53a3.3 3.3 0 00-.084-1.746l-.064-.195a7.193 7.193 0
 00-.257-.671l-1.387-3.27-.149-.445a2.08 2.08 0
 01-.093-.425l-.025-.223a2.065 2.065 0 01.59-1.696l.115-.114a8.33 8.33
 0 01.747-.666l.299-.235a.109.109 0
 01.126-.007c.04.025.06.071.049.117l-.119.53a3.3 3.3 0 00.083
 1.746l.064.195c.074.227.16.453.257.671l1.387
 3.27.15.445c.045.138.077.28.093.425l.025.223a2.065 2.065 0 01-.591
 1.696zm-3.997
 1.073l-.146.147c-.296.297-.612.579-.941.838l-.39.307a.12.12 0
 01-.192-.12l.154-.687a4.169 4.169 0 00-.105-2.205l-.08-.248a9.058
 9.058 0 00-.325-.848L9.91 10.28l-.188-.56a2.608 2.608 0
 01-.117-.532l-.032-.285a2.586 2.586 0
 01.74-2.124l.146-.147c.296-.297.612-.579.941-.838l.39-.307a.119.119 0
 01.138-.007.119.119 0 01.054.127l-.154.687a4.168 4.168 0 00.105
 2.205l.08.248c.094.287.204.572.325.848l1.75
 4.125.188.56c.057.173.097.352.117.532l.032.285a2.586 2.586 0 01-.74
 2.124zM9 16.148l-.114.114c-.234.236-.486.46-.747.666l-.299.235a.11.11
 0 01-.175-.11l.12-.53a3.3 3.3 0 00-.084-1.746l-.064-.195a7.181 7.181
 0 00-.257-.671l-1.387-3.27-.15-.445a2.076 2.076 0
 01-.093-.425l-.025-.223a2.065 2.065 0 01.591-1.696l.114-.114a8.34
 8.34 0 01.748-.666l.298-.235a.109.109 0
 01.127-.007c.04.025.059.071.049.117l-.12.53a3.3 3.3 0 00.084
 1.746l.064.195c.074.227.16.453.257.671l1.387
 3.27.149.445c.046.138.077.28.093.425l.025.223a2.065 2.065 0 01-.59
 1.696zM12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373 12-12S18.627
 0 12 0" />
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
