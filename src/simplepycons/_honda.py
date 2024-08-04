#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class HondaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "honda"

    @property
    def original_file_name(self) -> "str":
        return "honda.svg"

    @property
    def title(self) -> "str":
        return "Honda"

    @property
    def primary_color(self) -> "str":
        return "#E40521"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Honda</title>
     <path d="M23.902
 6.87c-.33-3.218-2.47-3.895-4.354-4.204-.946-.16-2.63-.3-3.716-.34-.946-.06-3.168-.09-3.835-.09-.657
 0-2.89.03-3.835.09-1.076.04-2.77.18-3.716.34C2.563 2.985.42 3.66.092
 6.87c-.08.877-.1 2.023-.09 3.248.03 2.031.2 3.406.3 4.363.07.657.338
 2.62.687 3.636.478 1.395.916 1.803 1.424 2.222.937.757 2.471.996 2.79
 1.056 1.733.31 5.24.368 6.784.368 1.544 0 5.05-.05 6.784-.368.329-.06
 1.863-.29 2.79-1.056.508-.419.946-.827
 1.424-2.222.35-1.016.628-2.979.698-3.636.1-.957.279-2.332.299-4.363.04-1.225.01-2.371-.08-3.248m-1.176
 5.4c-.19 2.57-.418 4.104-.747 5.22-.29.976-.637 1.623-1.165
 2.092-.867.787-2.063.956-2.76 1.056-1.514.23-4.055.3-6.057.3-2.002
 0-4.543-.08-6.057-.3-.697-.1-1.893-.269-2.76-1.056-.518-.469-.876-1.126-1.155-2.093-.329-1.105-.558-2.65-.747-5.22-.11-1.543-.09-4.054.08-5.4.258-2.011
 1.255-3.018 3.387-3.396.996-.18 2.34-.31 3.606-.37 1.016-.07 2.7-.1
 3.636-.09.936-.01 2.62.03 3.636.09 1.275.06 2.61.19 3.606.37
 2.142.378 3.139 1.395 3.388 3.397.199 1.345.229 3.856.11
 5.4m-5.202-8.39c-.548 2.462-.767 3.588-1.216 5.37-.428 1.715-.767
 3.298-1.335 4.065-.587.777-1.365.947-1.893
 1.006-.279.03-.478.04-1.066.05-.596
 0-.796-.02-1.075-.05-.528-.06-1.315-.229-1.892-1.006-.578-.767-.907-2.35-1.335-4.064-.47-1.773-.678-2.91-1.236-5.37
 0 0-.548.02-.797.04-.329.02-.588.05-.867.09.343 5.372.692 11.079
 1.126 16.13a21.983 21.983 0 002.39.169c.33-1.266.748-3.02
 1.207-3.767.378-.608.966-.677 1.295-.717.518-.07.956-.08
 1.165-.08.2-.01.637 0 1.165.08.33.05.917.11 1.295.717.47.747.877 2.5
 1.206 3.766 0 0 .358-.01 1.165-.05.41-.018.82-.058
 1.226-.12.458-5.39.785-10.728
 1.126-16.128-.28-.04-.538-.07-.867-.09-.23-.02-.787-.04-.787-.04z" />
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