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


class GoogleBigqueryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlebigquery"

    @property
    def original_file_name(self) -> "str":
        return "googlebigquery.svg"

    @property
    def title(self) -> "str":
        return "Google BigQuery"

    @property
    def primary_color(self) -> "str":
        return "#669DF6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google BigQuery</title>
     <path d="M5.676 10.595h2.052v5.244a5.892 5.892 0 0
 1-2.052-2.088v-3.156zm18.179 10.836a.504.504 0 0 1 0 .708l-1.716
 1.716a.504.504 0 0 1-.708 0l-4.248-4.248a.206.206 0 0
 1-.007-.007c-.02-.02-.028-.045-.043-.066a10.736 10.736 0 0 1-6.334
 2.065C4.835 21.599 0 16.764 0 10.799S4.835 0 10.8 0s10.799 4.835
 10.799 10.8c0 2.369-.772 4.553-2.066
 6.333.025.017.052.028.074.05l4.248 4.248zm-5.028-10.632a8.015 8.015 0
 1 0-8.028 8.028h.024a8.016 8.016 0 0 0 8.004-8.028zm-4.86 4.98a6.002
 6.002 0 0 0 2.04-2.184v-1.764h-2.04v3.948zm-4.5.948c.442.057.887.08
 1.332.072.4.025.8.025 1.2 0V7.692H9.468v9.035z" />
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
