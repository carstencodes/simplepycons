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


class PlausibleAnalyticsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plausibleanalytics"

    @property
    def original_file_name(self) -> "str":
        return "plausibleanalytics.svg"

    @property
    def title(self) -> "str":
        return "Plausible Analytics"

    @property
    def primary_color(self) -> "str":
        return "#5850EC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plausible Analytics</title>
     <path
 d="M12.1835.0017c-.6378-.0097-1.2884.022-1.7246.0996C8.601.424 7.035
 1.2116 5.7384 2.4782 4.406 3.7806 3.582 5.299 3.1818
 7.1929l-.1387.6445c-.0118 5.3872-.0233 10.7744-.035
 16.1617.2914.0081.591-.0392.8416-.0606 2.348-.2868 4.3442-1.7083
 5.4315-3.8651.2749-.5497.472-1.182.6094-1.9707.1135-.6691.1195-.8915.1016-4.3807l-.0176-3.6737.1425-.3574c.1972-.49.7425-1.0352
 1.2324-1.2324l.3574-.1426 3.3457-.0058c1.8401 0 3.4545-.025
 3.58-.0489.5854-.1135 1.2118-.6027
 1.4628-1.1464.0717-.1494.1671-.4415.209-.6387.0657-.3286.0604-.4186-.0352-.789-.2987-1.0993-1.3503-2.6234-2.4257-3.5136C16.6247
 1.1638 15.2798.4887
 13.828.1482c-.3824-.0866-1.0067-.1368-1.6445-.1465zm8.5369
 6.8006c-.0506.1798-.098.3662-.172.5215-.3358.7278-1.0382
 1.2776-1.8221
 1.4296-3.6737.0566-2.5392.0561-3.6737.0566l-3.248.0059-.2695.1074c-.3135.1262-.827.6397-.9531.9531l-.1074.2676.0175
 3.576c.0149 2.8888.007 3.5821-.0605 4.125a8.9918 8.9918 0 0 0
 1.5683.1386c4.9662.0001 8.992-4.0258 8.992-8.992a8.9918 8.9918 0 0
 0-.2715-2.1893Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/plausible/docs/blob/be5c93'''

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
