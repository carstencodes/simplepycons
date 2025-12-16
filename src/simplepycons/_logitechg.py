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


class LogitechGIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "logitechg"

    @property
    def original_file_name(self) -> "str":
        return "logitechg.svg"

    @property
    def title(self) -> "str":
        return "Logitech G"

    @property
    def primary_color(self) -> "str":
        return "#00B8FC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Logitech G</title>
     <path d="M12.5664 0C10.9101 0 9.352.3143
 7.8887.9414c-1.4794.6271-2.766 1.483-3.8594 2.5684-1.0935
 1.0854-1.9549 2.359-2.582 3.8222-.6432 1.4473-.9575 3-.9414 4.6563 0
 1.6563.3142 3.2164.9414 4.6797.8537 1.9702 2.6764 4.7711 6.4414
 6.3672C9.352 23.6784 10.91 24 12.5664 24v-4.9922c-.9809
 0-1.8977-.1848-2.75-.5547-1.6852-.7313-2.9903-2.0167-3.7383-3.7402-.7467-1.7207-.736-3.755
 0-5.4512.737-1.6981 2.0318-2.9977 3.7383-3.7383.8523-.3698
 1.7691-.5546 2.75-.5546Zm.17
 9.8418v4.9434h5.8124v5.8144h4.9453V9.8418Z" />
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
