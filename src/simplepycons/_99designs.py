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


class NinetyNineDesignsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "99designs"

    @property
    def original_file_name(self) -> "str":
        return "99designs.svg"

    @property
    def title(self) -> "str":
        return "99designs"

    @property
    def primary_color(self) -> "str":
        return "#FE5F50"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>99designs</title>
     <path d="M21.6504 13.7786c0 1.163-.943 2.1059-2.1059 2.1059-1.163
 0-2.1059-.943-2.1059-2.1059 0-1.163.943-2.1059 2.1059-2.1059 1.163 0
 2.1059.943 2.1059 2.106zm-7.557-3.5718c0 1.0842-.8775 2.0229-2.0228
 2.0229-1.117 0-2.0231-.9059-2.0231-2.0229s.906-2.0231
 2.0231-2.0231c1.117 0 2.0229.906 2.0229 2.0231zm-7.6605 0c0
 1.0822-.8759 2.0229-2.0231 2.0229-1.117
 0-2.0228-.9059-2.0228-2.0229s.9058-2.0231 2.0228-2.0231 2.0231.906
 2.0231 2.0231zm11.008 7.663c.9166.3985 2.2434.466
 3.1223.0578.392-.182.7534-.4776
 1.0847-.8858v.8776H24V6.0624h-2.4847v4.2717c-.707-.6853-1.4491-.9773-2.451-.9773-1.0589
 0-1.9244.3524-2.5844.9162.0003-.0221.0006-.044.0006-.0662
 0-2.435-1.9751-4.4098-4.4099-4.4098-1.6397 0-3.0704.8951-3.8305
 2.2236C7.4803 6.692 6.0493 5.797 4.4098 5.797 1.9748 5.797 0 7.7718 0
 10.2068c0 2.3312 1.81 4.2403 4.101 4.399L2.188
 17.9193H5.057c1.061-1.8422 2.1222-3.6844 3.1831-5.5266.712 1.244
 2.0124 2.1083 3.5216 2.213l-1.913 3.3136h2.8688l2.2372-3.8842c.0665
 1.5842.868 3.1305 2.4863 3.8345" />
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
