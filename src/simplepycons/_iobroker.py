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


class IobrokerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iobroker"

    @property
    def original_file_name(self) -> "str":
        return "iobroker.svg"

    @property
    def title(self) -> "str":
        return "ioBroker"

    @property
    def primary_color(self) -> "str":
        return "#3399CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ioBroker</title>
     <path d="M12 0c-.61 0-1.201.044-1.787.133v3.285a8.943 8.943 0
 013.574.004V.139A11.83 11.83 0 0012 0zM9.38.295C4.084 1.5.13 6.283.13
 12 .129 18.628 5.44 24 12 24s11.871-5.372
 11.871-12c0-5.717-3.953-10.499-9.246-11.705v3.34c3.575 1.113 6.18
 4.44 6.18 8.365 0 4.83-3.949 8.76-8.8 8.76-4.85
 0-8.804-3.93-8.804-8.76 0-3.924 2.605-7.247 6.18-8.365V.295zM12
 4.137c-.616 0-1.212.068-1.783.2V19.53A7.887 7.887 0 0012 19.73c.616 0
 1.211-.068 1.787-.2V4.343A7.65 7.65 0 0012 4.137Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ioBroker/awesome-iobroker/
blob/6ba42e9fcda7c88356e2f8c98f435ce7b02d4e37/images/awesome-iobroker.'''

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
