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


class RekaUiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rekaui"

    @property
    def original_file_name(self) -> "str":
        return "rekaui.svg"

    @property
    def title(self) -> "str":
        return "Reka UI"

    @property
    def primary_color(self) -> "str":
        return "#16A353"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Reka UI</title>
     <path d="M6.3478 1.3265c-.6864 0-1.1148.744-.77 1.3375l2.564
 4.4157h7.9478c1.1216 0 1.8502 1.26 1.2908 2.2322l-3.9539 6.8691
 3.4078 5.869a.8903.8903 0 0 0 .77.4431h5.5038c.711 0
 1.1352-.7922.741-1.384l-3.6294-5.4496c-.3177-.477-.089-1.1085.4021-1.362
 1.1318-.592 1.9681-1.4035
 2.5131-2.4347.5467-1.0343.8215-2.2223.8215-3.5667
 0-1.3443-.2748-2.5402-.8219-3.5899-.545-1.046-1.385-1.8689-2.5244-2.4681l-.0006-.0002c-1.1369-.6054-2.5976-.9114-4.388-.9114zM.9908
 7.5796c-.761 0-1.237.8232-.8574 1.4829l7.5494 13.1152c.3805.661
 1.3343.661 1.7148 0L16.947
 9.0625c.3796-.6597-.0963-1.4829-.8574-1.4829z" />
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
