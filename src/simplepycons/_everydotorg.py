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


class EverydotorgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "everydotorg"

    @property
    def original_file_name(self) -> "str":
        return "everydotorg.svg"

    @property
    def title(self) -> "str":
        return "Every.org"

    @property
    def primary_color(self) -> "str":
        return "#2BD7B0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Every.org</title>
     <path d="M18.151 9.36c0-4.467-3.728-7.855-8.517-7.855C4.278 1.505
 0 6.028 0 11.63c0 6.038 4.808 10.864 11.28 10.864 6.474 0 12.266-5.13
 12.72-11.848h-2.953c-.549 5.034-4.807 8.896-9.766 8.896-4.77
 0-8.31-3.502-8.31-7.912 0-3.975 2.953-7.174 6.663-7.174 3.104 0 5.546
 2.12 5.546 4.903 0 2.309-1.666 4.24-3.88 4.24v2.952c3.918 0
 6.851-3.274 6.851-7.192" />
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
