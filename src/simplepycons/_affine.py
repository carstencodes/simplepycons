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


class AffineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "affine"

    @property
    def original_file_name(self) -> "str":
        return "affine.svg"

    @property
    def title(self) -> "str":
        return "AFFiNE"

    @property
    def primary_color(self) -> "str":
        return "#1E96EB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AFFiNE</title>
     <path d="M11.9948
 1.3766c-.5962.0055-1.1835.3117-1.496.8633C9.3218 4.294 1.088
 18.5025.1273 20.2343c-.3903.9368.1537 2.0479 1.131
 2.3204.4061.1076.8337.0533 1.203.0664 5.3733.005 14.2336-.0065
 19.6234 0 .1562.0029.4285-.0014.6583-.0664.709-.1974 1.2348-.8705
 1.2558-1.6055.008-.2436-.0369-.4874-.125-.713-.1113-.2414-.1953-.3671-.287-.5312l-.545-.9434L14.321
 3.656l-.5449-.9434-.2734-.4726c-.1236-.2046-.2846-.39-.4805-.5352-.3071-.2255-.6696-.3314-1.0274-.3281Zm.006
 1.3008c.1467.0004.2936.0735.375.2148.1655.2769.6486 1.1385.8164 1.416
 1.8312 3.1736 4.1148 7.1296 6.3047 10.9221L10.3581 5.0895c.329-.5697
 1.1259-1.952
 1.2676-2.1973v-.002c.0814-.1421.2287-.2133.375-.2128zm-2.213 3.4668
 7.5548 7.8459c-.0189-.0085-.0377-.017-.0567-.0254L9.2858
 8.5232c.0712-.622.1933-1.2419.3496-1.8555zM8.3698 8.535 4.2213
 21.3203c-.5326-.0002-1.2787.0002-1.7598
 0-.1099-.0007-.6827.0033-.7579-.004-.2804-.005-.478-.3305-.371-.5878.6398-1.1206
 4.1786-7.2439 7.0372-12.1936Zm.8437 1.205 5.5743
 3.4318-5.504-2.2774A9.1593 9.1593 0 0 1 9.2135 9.74zm-.8594
 1.377-.6972 9.465c-.7194.3027-1.4733.537-2.2403.7247zm1.1524.9083
 3.5528 1.2246h-3.086a7.1294 7.1294 0 0
 1-.33-.7734c-.0508-.1501-.0956-.3-.1368-.4512zm-.5527.8516c.0161.0437.0318.0873.0488.1308l.834
 6.338c-.3456.2621-.7092.496-1.088.707zm1.8652 1.168h2.3653c.18 0
 .2928.1935.2031.3496l-1.1836 2.0488a.233.233 0 0 1-.4043
 0h-.002l-1.1816-2.0488c-.0904-.1561.0224-.3496.203-.3496zm3.6778.0156a7.161
 7.161 0 0 1 .832.0996 7.847 7.847 0 0 1 .463.1094l-2.8419
 2.4668zm2.381.58a9.1839 9.1839 0 0 1 1.0566.5274l-5.879
 3.1739zm-6.8889.2579 1.543 2.6719a7.1154 7.1154 0 0 1-.5039.67 7.8136
 7.8136 0 0
 1-.3223.3456zm8.965.9453c.2738.2038.5382.4222.797.6485l.9863
 1.0234L10.028 20.168c.0195-.0135.0392-.0274.0586-.041zm2.4473
 2.6856c.3799.6581.848 1.4656 1.1934
 2.0645.0608.0998.0519.1041.0742.1367.0948.2291-.0458.5041-.2793.5742-.0303.0015-.0577.0146-.0918.0118-.0057.005-.129.0039-.2129.0039-3.7797-.001-8.9869-.0003-13.7893
 0z" />
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
