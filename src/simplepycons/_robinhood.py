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


class RobinhoodIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "robinhood"

    @property
    def original_file_name(self) -> "str":
        return "robinhood.svg"

    @property
    def title(self) -> "str":
        return "Robinhood"

    @property
    def primary_color(self) -> "str":
        return "#00C805"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Robinhood</title>
     <path d="M20.0559.6412C19.5739.222 18.873.0255
 17.786.0015c-.9876-.0218-2.16.1922-3.4893.6288-.1987.0699-.3582.1812-.4994.3188a64.271
 64.271 0 0 0-3.9086 4.004l-.0959.1048a.0937.0937 0 0
 0-.0113.107c.02.035.0619.0525.1011.0437l.1395-.0306c2.0022-.4279
 4.0236-.7554 6.0084-.9715a.4605.4605 0 0 1 .3626.1179.4657.4657 0 0 1
 .1499.3515c-.0323 1.9693.0392 3.9474.2144
 5.8795l.0105.1267a.0927.0927 0 0 0
 .0706.0808c.006.0022.013.0022.0218.0044a.1.1 0 0 0
 .0784-.0394l.0715-.1025a55.8263 55.8263 0 0 1
 3.614-4.6112c.1437-.1637.1812-.2664.2074-.4148.401-2.5719-.2206-4.4757-.7758-4.9582Zm-4.3967
 5.528-.0026-.1222a.0945.0945 0 0 0-.061-.0852.0952.0952 0 0
 0-.102.0263l-.081.0917c-3.3995 3.932-6.2577 8.2942-8.4927
 12.9686l-.0523.109a.093.093 0 0 0 .0149.1049.095.095 0 0 0
 .0653.0284.123.123 0 0 0 .0375-.0065l.1116-.0459c1.9098-.7903
 3.8597-1.4759 5.7957-2.037a.4419.4419 0 0 0 .2693-.2227c.849-1.6549
 2.8207-4.86
 2.8207-4.86.0497-.072.0366-.179.0366-.179s-.3382-3.8316-.36-5.7704zM6.7317
 17.341c.068-.131.3783-.7292.448-.8624l.013-.024c2.0781-3.919
 4.6112-7.6174 7.526-10.9884l.081-.0939a.0974.0974 0 0 0
 .0105-.1047.094.094 0 0 0-.0941-.048l-.122.0174A60.3806 60.3806 0 0 0
 8.8367 6.322c-.19.0524-.312.1769-.3382.2052a64.6783 64.6783 0 0
 0-4.02 5.3534c-.061.0939-.0829.2162-.0672.3166.013.0982.312
 2.4016.7662 4.17-1.1262 3.2421-2.133 7.5148-2.133 7.5148a.0947.0947 0
 0 0 .0131.0808.0888.0888 0 0 0 .0741.0371h.6416a.0987.0987 0 0 0
 .0923-.0612l.0436-.12c.6546-1.786 1.4017-3.55
 2.2271-5.2704.1918-.3974.5954-1.2074.5954-1.2074Zm3.8257
 1.489-.1595.0525c-1.026.3405-2.5435.8667-3.906
 1.4933-.0723.035-.1202.131-.1202.131-.0262.059-.0567.131-.0915.2117l-.0044.011c-.1534.3471-.3626.8689-.4541
 1.0829l-.0698.1681a.067.067 0 0 0 .0175.0764.0615.0615 0 0 0
 .0453.0197c.0087 0
 .02-.0022.0305-.0065l.1639-.0786c.3739-.1769.8455-.4454
 1.3388-.6812l.0175-.0087a885.5338 885.5338 0 0 0
 2.6411-1.2554s.1029-.0546.1552-.1572l.4785-.9606a.0703.0703 0 0
 0-.0087-.0765.0685.0685 0 0 0-.074-.0218z" />
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
